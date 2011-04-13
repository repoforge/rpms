# $Id$
# Authority: matthias

Summary: Small application for displaying the contents of a DVD
Name: lsdvd
Version: 0.16
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://untrepid.com/lsdvd/
Source: http://dl.sf.net/acidrip/lsdvd-%{version}.tar.gz
Patch0: lsdvd-0.16-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, automake
BuildRequires: libdvdread-devel

%description
Lsdvd is a c application for reading the contents of a DVD and printing the
contents to your terminal. Lsdvd uses libdvdread, the most popular dvd
reading library for *nix


%prep
%setup
%patch0 -p1 -b .build
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
%{_mandir}/man1/lsdvd.1*


%changelog
* Mon May  8 2006 Matthias Saou <http://freshrpms.net/> 0.16-2
- Rebuild with latest tarball from sf.net, as apparently the original 0.16
  source was replaced after 3 days by a "fixed" source with the same file name.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 0.16-1
- Update to 0.16.
- Update URL.
- Update build patch, keep fixed libdvdread include detection.
- Include newly added man page.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.15-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 0.15-1
- Initial RPM release.

