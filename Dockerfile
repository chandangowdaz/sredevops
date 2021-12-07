FROM public.ecr.aws/amazonlinux/amazonlinux:latest

RUN yum update -y && yum install -y httpd

RUN echo 'Hello World from Docker' > /var/www/html/index.html

# Configure apache

RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
 echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
 echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
 chmod 755 /root/run_apache.sh

EXPOSE 8083

CMD /root/run_apache.sh
