import java.io.*;
import java.util.*;



class SampleGenerate {
  static List<String[]> info = new ArrayList<>();


  public static void main(String[] args) {
    Map<String, Integer> map20 = generateMap(50);
    List<String> constraints20 = generateConstraint(map20);
    System.out.println(constraints20.size());
    writeFile(constraints20);
    Comparator<String[]> compare = new MyComparator();
    Collections.sort(info, compare);
    optimal(info);
  }
  public static void optimal(List<String[]> lst){
    for(String[] arr : lst){
      System.out.print(arr[0] + " ");
    }
  }
  public static void writeFile(List<String> constraints) {
    for(String str: constraints) {
       System.out.println(str);
    }
  }

  /**
  * Generate a list of W wizard names with their ages generated.
  */
  public static Map<String, Integer> generateMap(int W) {
    HashMap<String, Integer> map = new HashMap<>();
    Random rand = new Random();
    for(int i = 0; i < W; i++) {
      String name = "Wizard" + Integer.toString(i);
      int age = rand.nextInt(100) + 1;
      System.out.println(name + " " + age);
      map.put(name, age);
      String[] tmp = {name, Integer.toString(age)};
      info.add(tmp);
    }
    return map;
  }


  /**
  *  Generate a list of constraints from the ages and corresponding names of wizards.
  */
  public static List<String> generateConstraint(Map<String, Integer> map) {
    ArrayList<String> result = new ArrayList<>();
    int length = map.size();
    String[] names = Arrays.copyOf(map.keySet().toArray(),map.keySet().toArray().length, String[].class);
    for (int i = 0; i < 499; i += 1) {
      String constraint = "";
      Random rand = new Random();
      int randNum = rand.nextInt(100);
      int index1 = rand.nextInt(length - 1);
      int index2 = rand.nextInt(length - 1);
      int index3 = rand.nextInt(length - 1);
      String name1 = names[index1];
      String name2 = names[index2];
      String name3 = names[index3];
      int age1 = map.get(name1);
      int age2 = map.get(name2);
      int age3 = map.get(name3);
      Comparator<String[]> compare = new MyComparator();
      List<String[]> chosen = new ArrayList<>();
      String[] element1 = {name1, Integer.toString(age1)};
      String[] element2 = {name2, Integer.toString(age2)};
      String[] element3 = {name3, Integer.toString(age3)};
      chosen.add(element1);
      chosen.add(element2);
      chosen.add(element3);
      Collections.sort(chosen, compare);
      if (chosen.get(0)[1] == chosen.get(1)[1] && chosen.get(0)[1] == chosen.get(2)[1]) {
           constraint = chosen.get(0)[0] + " " +  chosen.get(1)[0] + " " +  chosen.get(2)[0];
      } else if (chosen.get(0)[1] == chosen.get(1)[1] || chosen.get(1)[1] == chosen.get(2)[1]){
          if(randNum % 2 == 1) {
            constraint = chosen.get(0)[0] + " " +  chosen.get(1)[0] + " " +  chosen.get(2)[0];
          } else {
            constraint = chosen.get(1)[0] + " " +  chosen.get(2)[0] + " " +  chosen.get(0)[0];
          }
      } else {
        if(randNum % 4 == 1) {
          constraint = chosen.get(0)[0] + " " +  chosen.get(1)[0] + " " +  chosen.get(2)[0];
        } else if (randNum % 4 == 2) {
          constraint = chosen.get(1)[0] + " " +  chosen.get(0)[0] + " " +  chosen.get(2)[0];
        } else if (randNum % 4 == 3) {
          constraint = chosen.get(1)[0] + " " +  chosen.get(2)[0] + " " +  chosen.get(0)[0];
        } else {
          constraint = chosen.get(2)[0] + " " +  chosen.get(1)[0] + " " +  chosen.get(0)[0];
        }
      }
      result.add(constraint);
    }
    return result;
  }

/**
* This is a self-defined comparator which compares array of strings according to the age.
*/

  static class MyComparator implements Comparator<String[]>{
    @Override
    public int compare(String[] a, String[] b){
      if(a[1].equals(b[1])){
        return a[0].compareTo(b[0]);
      }
      return Integer.parseInt(a[1]) - Integer.parseInt(b[1]);
    }
  }


}
