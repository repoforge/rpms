# $Id$
# Authority: dag

### EL6 ships with dejavu-fonts-common-2.30-2.el6
# ExclusiveDist: el2 el3 el4 el5
# Dist: nodist

%define real_name dejavu-ttf

Summary: DejaVu TrueType fonts
Name: dejavu-fonts
Version: 2.20
Release: 1%{?dist}
License: Redistributable, with restrictions
Group: User Interface/X
URL: http://dejavu.sourceforge.net/

Source: http://dl.sf.net/dejavu/dejavu-ttf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Conflicts: fontconfig >= 2.3.0

%description
The DejaVu TrueType fonts are a font family based on the Bitstream Vera Fonts
release 1.10. Its purpose is to provide a wider range of characters while
maintaining the original look and feel through the process of collaborative
develop

%prep
%setup -n %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/dejavu/
%{__install} -p -m0644 *.ttf %{buildroot}%{_datadir}/fonts/dejavu/
touch %{buildroot}%{_datadir}/fonts/dejavu/fonts.cache-1

%clean
%{__rm} -rf %{buildroot}

%post
%{_bindir}/fc-cache -f %{_datadir}/fonts/dejavu/ || :

%postun
if [ $1 -eq 0 ]; then
	%{_bindir}/fc-cache -f %{_datadir}/fonts/dejavu/ || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS LICENSE NEWS README *.txt
%{_datadir}/fonts/dejavu/
%ghost %{_datadir}/fonts/dejavu/fonts.cache-1

%changelog
* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 2.20-1
- Updated to release 2.20.

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Wed Apr 04 2007 Dag Wieers <dag@wieers.com> - 2.16-1
- Updated to release 2.16.

* Fri Feb 16 2007 Dag Wieers <dag@wieers.com> - 2.14-1
- Initial package. (using DAR)
