# $Id$
# Authority; dag

Summary: Tool to find duplicate files in a given set of directories
Name: fdupes
Version: 1.40
Release: 1
License: MIT
Group: Applications/File
URL: http://netdial.caribe.net/~adrian2/fdupes.html

Source: http://netdial.caribe.net/~adrian2/programs/%{name}-%{version}.tar.gz
Patch0: fdupes-1.40-destdir.patch
Patch1: fdupes-1.40-string.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
FDUPES is a program for identifying duplicate files residing within specified
directories.

%prep
%setup
%patch0 -p1
%patch1 -p1

%{__perl} -pi.orig -e 's|-Wall|%{optflags}|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install DESTDIR="%{buildroot}" INSTALLDIR="%{_bindir}" MANPAGEDIR="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS README TODO
%doc %{_mandir}/man1/fdupes.1*
%{_bindir}/fdupes

%changelog
* Tue Sep 30 2008 Dag Wieers <dag@wieers.com> - 1.40-1
- Initial package. (based on fedora)
