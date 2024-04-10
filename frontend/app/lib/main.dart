import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override 
  Widget build(BuildContext context) {
    const String appTitle = "2024 Election Hub";
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: appTitle,
      home: Scaffold(
        backgroundColor: Colors.purpleAccent,
        body: Center( 
          child: Container(
            height: 300,
            width: 300,
            decoration: BoxDecoration( 
              color: Color.fromRGBO(83, 109, 254, 1),
              borderRadius: BorderRadius.circular(20),
            ),
            padding: const EdgeInsets.all(25),
            child: Icon( 
              Icons.favorite,
              color: Colors.white,
              size: 64
            )   
          )
        ),
      ),
    );
  }
  
}
