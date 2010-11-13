# $Id$
# Authority: dag
# Upstream: Joakim Andersson <ja$morrdusk,net>


Summary: Log colorizer that makes log checking easier
Name: colortail
Version: 0.3.0
Release: 2.2%{?dist}
Group: Applications/File
License: GPL
URL: http://www.student.hk-r.se/~pt98jan/colortail.html

Source: ftp://ftp.be.netbsd.org/pub/NetBSD/packages/distfiles/colortail-%{version}.tar.gz
Patch0: colortail-0.3.0-gcc3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, automake, autoconf

%description
Colortail is a log colorizer that makes log checking easier. It works
like tail but can read one or more configuration files. In which it's
specified which patterns result in which colors.

%prep
%setup
%{!?rh6:%patch0 -b .gcc3}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING example-conf/conf.* NEWS README TODO
%{_bindir}/colortail

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0-2.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.0-2
- Modified the source url. Project page doesn't exist anymore.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Added example config files. (Adrian Reber)

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.3.0-0
- Initial package. (using DAR)
