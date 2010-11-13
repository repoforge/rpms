# $Id$
# Authority: dag

Summary: Tool for finding common mistakes in LaTeX documents
Name: lacheck
Version: 1.26
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.ctan.org/get/support/lacheck/

Source: http://www.ctan.org/get/support/lacheck/lacheck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
lacheck is a general purpose consistency checker for LaTeX documents.
It reads a LaTeX document and displays warning messages, if it finds
bad sequences. It should be noted, that the badness is very subjective.

lacheck is designed to help find common mistakes in LaTeX documents,
especially those made by beginners.

%prep
%setup

%build
%{__make} lacheck lacheck.1 prefix="%{_prefix}" CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 lacheck %{buildroot}%{_bindir}/lacheck
%{__install} -Dp -m0644 lacheck.1 %{buildroot}%{_mandir}/man1/lacheck.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc lacheck.hlp
%doc %{_mandir}/man1/lacheck.1*
%{_bindir}/lacheck

%changelog
* Mon Nov 24 2008 Geerd-Dietger Hoffmann <ribalba@gmail.com> - 1.26-1
- Initial package.
