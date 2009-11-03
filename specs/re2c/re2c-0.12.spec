# $Id$
# Authority: dag

Summary: Tool for generating C-based recognizers from regular expressions
Name: re2c
Version: 0.12.3
Release: 1%{?dist}
License: MIT
Group: Development/Tools
URL: http://re2c.sourceforge.net/

Source: http://dl.sf.net/re2c/re2c-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
re2c is a great tool for writing fast and flexible lexers. It has
served many people well for many years and it deserves to be
maintained more actively. re2c is on the order of 2-3 times faster
than a flex based scanner, and its input model is much more
flexible.

%prep
%setup

%build
%configure
%{__make} re2c

### Regenerate file scanner.cc
./re2c -b scanner.re >scanner.cc
%{__rm} -f re2c scanner.o
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 re2c %{buildroot}%{_bindir}/re2c
%{__install} -Dp -m0644 re2c.1 %{buildroot}%{_mandir}/man1/re2c.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README examples/ doc/* lessons/
%doc %{_mandir}/man1/re2c.1*
%{_bindir}/re2c

%changelog
* Wed Sep 12 2007 Dag Wieers <dag@wieers.com> - 0.12.3-1
- Updated to release 0.12.3.

* Wed May 23 2007 Dag Wieers <dag@wieers.com> - 0.12.1-1
- Updated to release 0.12.1.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.12.0-1
- Initial version.
