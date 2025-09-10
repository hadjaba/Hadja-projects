package FocusPal;

import java.io.*;
import java.util.*;

public class FocusPal {

    private static final String STREAK_FILE = "streak.txt";
    private static List<String> tasks = new ArrayList<>();
    private static int streak = 0;

    public static void main(String[] args) throws IOException, Exception {
        Scanner scanner = new Scanner(System.in);

        loadStreak();

        System.out.println("🌟 Welcome to FocusPal! 🌟");
        System.out.println("Today's Productivity Streak: " + streak + " days");

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Add task");
            System.out.println("2. View tasks");
            System.out.println("3. Start focus timer (25 min)");
            System.out.println("4. Simulate website block");
            System.out.println("5. Save streak and exit");
            System.out.print("Choose an option: ");

            int option = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (option) {
                case 1 -> {
                    System.out.print("Enter task: ");
                    String task = scanner.nextLine();
                    tasks.add(task);
                    System.out.println("Task added ✅");
                }
                case 2 -> {
                    System.out.println("Your tasks:");
                    for (int i = 0; i < tasks.size(); i++) {
                        System.out.println((i + 1) + ". " + tasks.get(i));
                    }
                }
                case 3 -> {
                    System.out.println("🕒 Focus timer started! 25 minutes...");
                    System.out.println("(Pretend you're being productive 🧠)");
                    // Thread.sleep(1500000); // for real 25 min
                    Thread.sleep(3000); // shorter for demo
                    System.out.println("✅ Timer done! Great job.");
                    streak++;
                }
                case 4 -> {
                    System.out.println("🚫 Access to social media blocked during focus time.");
                }
                case 5 -> {
                    saveStreak();
                    System.out.println("Streak saved. Goodbye 👋");
                    return;
                }
                default -> System.out.println("Invalid option.");
            }
        }
    }

    private static void loadStreak() {
        try (BufferedReader reader = new BufferedReader(new FileReader(STREAK_FILE))) {
            streak = Integer.parseInt(reader.readLine());
        } catch (IOException | NumberFormatException e) {
            streak = 0; // start from 0 if file missing/corrupt
        }
    }

    private static void saveStreak() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(STREAK_FILE))) {
            writer.write(String.valueOf(streak));
        } catch (IOException e) {
            System.out.println("Error saving streak.");
        }
    }
}