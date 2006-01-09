# $Id$
# Authority: matthias

Summary: Small application for displaying the contents of a DVD
Name: lsdvd
Version: 0.15
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://untrepid.com/acidrip/lsdvd.html
Source: http://dl.sf.net/acidrip/lsdvd-%{version}.tar.gz
Patch: lsdvd-0.15-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, automake
BuildRequires: libdvdread-devel

%description
Lsdvd is a c application for reading the contents of a DVD and printing the
contents to your terminal. Lsdvd uses libdvdread, the most popular dvd
reading library for *nix


%prep
%setup
%patch -p1 -b .build
%{__aclocal}
%{__automake} --add-missing --copy --force --gnu --include-deps Makefile
%{__autoconf}


%build
%configure
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/lsdvd


%changelog
* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 0.15-1
- Initial RPM release.

