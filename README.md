# Python Learning Portfolio

This repository shows my progress building small Python projects with a practical focus. Each project helped me work through a specific concept, from basic scripting and file handling to GUI apps, automation, concurrency, networking and security basics.

The goal is not to present oversized applications, but clear projects that show how I approach problems, structure code, and improve step by step.

## Focus Areas

- Python fundamentals and scripting
- File handling and CSV processing
- GUI development with Tkinter and Turtle
- Basic automation
- Data processing with pandas
- Concurrency with threads and processes
- Networking with sockets, HTTP and FTP
- Introductory security concepts

## Repository Structure

- `projects/` contains each project in its own folder.
- Projects with external dependencies include their own `requirements.txt`.

## Projects

| #   | Project                                                                | Level        | Concepts                                                         |
| --- | ---------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------- |
| 01  | [Blind Auction](projects/01-blind-auction)                             | Basic        | Dictionaries, loops, conditionals, console input                 |
| 02  | [Calculator](projects/02-calculator)                                   | Basic        | Functions, dictionaries, loops, console menus                    |
| 03  | [Blackjack](projects/03-blackjack)                                     | Basic        | Lists, functions, randomization, game loops                      |
| 04  | [Number Guessing](projects/04-number-guessing)                         | Basic        | Scope, constants, conditionals, loops                            |
| 05  | [Debugging Exercises](projects/05-debugging-exercises)                 | Basic        | Debugging, reading tracebacks, control flow                      |
| 06  | [Higher Lower Game](projects/06-higher-lower-game)                     | Basic        | Dictionaries, modules, randomization, loop control               |
| 07  | [Turtle Graphics](projects/07-turtle-graphics)                         | Basic        | Turtle graphics, randomization, drawing loops                    |
| 08  | [Turtle Race](projects/08-turtle-race)                                 | Basic        | Event handling, Turtle graphics, randomization                   |
| 09  | [File I/O and Mail Merge](projects/09-file-io-and-mail-merge)          | Basic        | File paths, reading, writing, template replacement               |
| 10  | [Tkinter Mile Converter](projects/10-tkinter-mile-converter)           | Basic        | Tkinter, GUI layout, callbacks                                   |
| 11  | [Coffee Machine Procedural](projects/11-coffee-machine-procedural)     | Intermediate | Procedural design, dictionaries, resource accounting             |
| 12  | [OOP Coffee Machine](projects/12-oop-coffee-machine)                   | Intermediate | Classes, objects, composition, methods                           |
| 13  | [Quiz Game OOP](projects/13-quiz-game-oop)                             | Intermediate | Classes, object composition, quiz state                          |
| 14  | [Snake Game](projects/14-snake-game)                                   | Intermediate | OOP, Turtle graphics, collision detection, game loop             |
| 15  | [Pong Game](projects/15-pong-game)                                     | Intermediate | OOP, collision detection, keyboard events, game loop             |
| 16  | [Turtle Crossing Game](projects/16-turtle-crossing-game)               | Intermediate | OOP, game difficulty, collision detection                        |
| 17  | [Snake Game With Persistence](projects/17-snake-game-with-persistence) | Intermediate | File persistence, game state, OOP                                |
| 18  | [Pandas Data Analysis](projects/18-pandas-data-analysis)               | Intermediate | CSV processing, pandas, data aggregation                         |
| 19  | [US States Quiz](projects/19-us-states-quiz)                           | Intermediate | CSV data, pandas, Turtle graphics, GUI interaction               |
| 20  | [NATO Alphabet](projects/20-nato-alphabet)                             | Intermediate | Dictionary comprehensions, pandas, input validation              |
| 21  | [Pomodoro Timer](projects/21-pomodoro-timer)                           | Intermediate | Tkinter, timers, UI state, callbacks                             |
| 22  | [Password Manager](projects/22-password-manager)                       | Intermediate | Tkinter, JSON persistence, password generation, search           |
| 23  | [Flash Card App](projects/23-flash-card-app)                           | Intermediate | Tkinter, CSV data, state persistence, language learning UI       |
| 24  | [Email Quotes Automation](projects/24-email-quotes-automation)         | Intermediate | SMTP, dates, file input, automation                              |
| 25  | [Data Processing Concurrency](projects/25-data-processing-concurrency) | Advanced     | Threads, processes, multiprocessing, concurrency, parallelism    |
| 26  | [Thread Safe Inventory](projects/26-thread-safe-inventory)             | Advanced     | Threads, shared state, race conditions, locks, synchronization   |
| 27  | [TCP UDP Socket Servers](projects/27-tcp-udp-socket-servers)           | Advanced     | Sockets, TCP, UDP, threading, client-server architecture         |
| 28  | [HTTP FTP Inventory API](projects/28-http-ftp-inventory-api)           | Advanced     | HTTP server, FTP upload, CSV inventory, API clients              |
| 29  | [HTTPS Crypto Integrity](projects/29-https-crypto-integrity)           | Advanced     | HTTPS, certificates, hashing, AES-GCM encryption, authentication |

## How to Run

Most projects can be run from their own folder with Python:

```bash
python main.py
```

Some projects use a different entry file. In those cases, the project README includes the correct command.

If a project has external dependencies, install them from that project's folder:

```bash
pip install -r requirements.txt
```

## Notes

The projects are intentionally small and focused. Earlier ones are simple because they reflect the basics, while later projects introduce more structure, external libraries, networking, concurrency and security-related topics.
