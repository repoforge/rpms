# $Id$

Summary: Perl module for creating rpm packages of other perl modules
Name: perl-RPM-Specfile
Version: 1.13
Release: 1.fr
License: GPL or Artistic
Group: Development/Tools
Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHIPT/RPM-Specfile-%{version}.tar.gz
URL: http://search.cpan.org/dist/RPM-Specfile/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl
BuildRequires: perl
BuildArch: noarch

%description
Simple module for creation of RPM Spec files.  Used by cpanflute2 to turn CPAN
tarballs into RPM modules.
See the included script cpanflute2 for usage; documentation coming soon.

%prep
%setup -q -n RPM-Specfile-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"
make test

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT$installarchlib
%makeinstall PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
rm -f `find $RPM_BUILD_ROOT -type f -name perllocal.pod -o -name .packlist`

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT -type f -print | \
  sed "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-, root, root, -)
%doc Changes README

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.13-1.fr
- Update to 1.13.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar  6 2003 Matthias Saou <http://freshrpms.net/>
- Stole the package, minor cosmetic changes :-)

* Sun Feb  9 2003 Ville Skyttä <ville.skytta at iki.fi> 1.11-1.fedora.1
- First Fedora release.

