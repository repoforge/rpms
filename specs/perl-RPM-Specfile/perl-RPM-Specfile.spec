# $Id$
# Authority: matthias
# ExclusiveDist: el2 rh7 rh9 el3 fc1

Summary: Perl module for creating rpm packages of other perl modules
Name: perl-RPM-Specfile
Version: 1.13
Release: 1
License: GPL or Artistic
Group: Development/Tools
Source: http://www.cpan.org/modules/by-module/RPM/RPM-Specfile-%{version}.tar.gz
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
%setup -n RPM-Specfile-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL
%{__make} %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} test

%install
%{__rm} -rf %{buildroot}
eval `%{__perl} '-V:installarchlib'`
%{__mkdir_p} %{buildroot}$installarchlib
%makeinstall PERL_INSTALL_ROOT=%{buildroot}
%{__rm} -f `find %{buildroot} -type f -name perllocal.pod -o -name .packlist`

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find %{buildroot} -type f -print | \
  sed "s@^%{buildroot}@@g" > %{name}-%{version}-%{release}-filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-, root, root, 0755)
%doc Changes README

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.13-1
- Update to 1.13.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar  6 2003 Matthias Saou <http://freshrpms.net/>
- Stole the package, minor cosmetic changes :-)

* Sun Feb  9 2003 Ville Skyttä <ville.skytta at iki.fi> 1.11-1.fedora.1
- First Fedora release.

