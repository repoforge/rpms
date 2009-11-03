# $Id$
# Authority: dag
# Upstream: Oskar Liljeblad <oskar@osk.mine.nu>

Summary: Execute a command when the content of a directory changes
Name: dnotify
Version: 0.18.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/File
URL: http://www.student.lu.se/~nbi98oli/dnotify.html

Source: http://www.student.lu.se/~nbi98oli/src/dnotify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
dnotify is a simple program that makes it possible to execute a command
every time the contents of a specific directory change in linux. It is run
from the command line and takes two arguments: one or more directories to
monitor and a command to execute whenever a directory has changed. Options
control what events to trigger on: when a file was read in the directory,
when one was created, deleted and so on.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%doc %{_mandir}/man1/dnotify.1*
%{_bindir}/dnotify

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.18.0-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 06 2004 Dag Wieers <dag@wieers.com> - 0.18.0-1
- Initial package. (using DAR)
