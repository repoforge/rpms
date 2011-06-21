# $Id$
# Authority: dag
# Upstream: John Peacock <jpeacock$rowman,com>

### EL6 ships with perl-version-0.77-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name version

Summary: Perl module that implements for Version Objects
Name: perl-version
Version: 0.91
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/version/

#Source: http://www.cpan.org/modules/by-module/version/version-%{real_version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/J/JP/JPEACOCK/version-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{real_version}-%{release}-root

BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.005

%description
version is a Perl module that implements for Version Objects.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/version.3pm*
%doc %{_mandir}/man3/version::Internals.3pm*
%{perl_vendorarch}/auto/version/
%{perl_vendorarch}/version/
%{perl_vendorarch}/version.pm
%{perl_vendorarch}/version.pod

%changelog
* Tue Jun 21 2011 David Hrbáč <david@hrbac.cz> - 0.91-1
- new upstream release

* Fri Jun 03 2011 David Hrbáč <david@hrbac.cz> - 0.90-1
- new upstream release

* Fri Jun 03 2011 David Hrbáč <david@hrbac.cz> - 0.89-1
- new upstream release

* Mon Dec 20 2010 David Hrbáč <david@hrbac.cz> - 0.87-1
- new upstream release

* Mon Nov 29 2010 David Hrbáč <david@hrbac.cz> - 0.86-1
- new upstream release

* Tue Oct 26 2010 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Mon Oct 25 2010 David Hrbáč <david@hrbac.cz> - 0.84-1
- new upstream release

* Mon Oct 18 2010 David Hrbáč <david@hrbac.cz> - 0.83-1
- new upstream release

* Tue Jul 13 2010 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Wed Jul 27 2009 Christoph Maser <cmr@financial.com> - 0.77.1-1
- Updated to version 0.77.1.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.76-1
- Updated to version 0.76.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.74-1
- Updated to release 0.74.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.72.3-1
- Initial package. (using DAR)
