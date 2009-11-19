# $Id$
# Authority: shuff
# Upstream: Dean Jones <deanjones$cleancode,org>

Summary: A command line SMTP client that's simple
Name: email
Version: 3.1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.pell.portland.or.us/~orc/Code/discount/

Source: http://www.cleancode.org/downloads/email/email-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: glibc-devel
BuildRequires: openssl-devel
Requires: gnupg

Provides: %{_bindir}/email

%description
Email is a program for the Unix environment that sends messages. You may think
that this has already been done, and it has, but not with the quality and
enhancements that email has! Have you ever wanted to send email from the
command line using your SMTP server instead of sendmail? Have you ever wanted
to send email without entering a confusing menu application and you only wanted
to push a few command line options to route your email to the SMTP server of
your choice? Did you want to encrypt that email with gpg before it was sent but
wanted the email client to do it for you? If you answered yes to all of these
questions, then email is for you. You can now send email via the command line
to remote SMTP servers. You can have it encrypted to the recipient of your
choice. This and many other possibilities are easily implemented with email.

Email boasts a lot of other qualities as well.

    * Email supports SMTP Authentication.
    * Email makes it possible to send to multiple recipients and also CC and
      BCC multiple recipients.
    * You can use an address book that is in an easy to format method.
    * You are also able to send attachments using a swift flick on the command
      line to specifying multiple files.
    * Personalized signature file with dynamic options.


%prep
%setup

%build
export CFLAGS="%{optflags} -I../include -I../dlib/include"
export LDFLAGS="-L../dlib"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog INSTALL README RFC821 THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%dir %{_sysconfdir}/email/
%config(noreplace) %{_sysconfdir}/email/*

%changelog
* Thu Nov 19 2009 Steve Huff <shuff@vecna.org> - 3.1.2-1
- Initial package.
