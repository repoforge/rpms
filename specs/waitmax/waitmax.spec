# $Id$
# Authority: dag

Summary: Allow program to run at most a specified amount of time
Name: waitmax
Version: 1.1
Release: 1
License: GPL
Group: Applications/System
URL: http://mathias-kettner.de/waitmax.html

Source: http://mathias-kettner.de/download/waitmax-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Waitmax executes program in a new process. If process has not exited
after at most maxtime seconds, it is being killed with signal TERM.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS
%doc %{_mandir}/man1/waitmax.1*
%{_bindir}/waitmax

%changelog
* Sun Apr 06 2008 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
