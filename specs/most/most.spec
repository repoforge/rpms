# $Id$
# Authority: dag
# Upstream: John E. Davis <davis$space,mit,edu>

Summary: text viewer similar to more or less, but with additional capabilities
Name: most
Version: 4.9.5
Release: 1
License: GPL
Group: Applications/Text
URL: ftp://space.mit.edu/pub/davis/most/

Source: ftp://space.mit.edu/pub/davis/most/most-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: slang-devel

%description
most is a paging program that displays, one windowful at a time, the
contents of a file on a terminal. It pauses after each windowful and
prints on the window status line the screen the file name, current line
number, and the percentage of the file so far displayed.

%prep
%setup

%build
%{__perl} -pi.orig -e 's|/usr/lib|%{_libdir}|' configure
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/objs/most %{buildroot}%{_bindir}/most
%{__install} -Dp -m0644 most.1 %{buildroot}%{_mandir}/man1/most.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc COPYRIGHT README *.doc *.rc *.txt
%doc %{_mandir}/man1/most.1*
%{_bindir}/most

%changelog
* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 4.9.5-1
- Initial package. (using DAR)
