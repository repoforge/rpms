# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Local

Summary: Efficiently compute time from local and GMT time
Summary: Perl module named Time-Local
Name: perl-Time-Local
Version: 1.2000
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Local/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Time-Local-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Efficiently compute time from local and GMT time.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Time::Local.3pm*
%dir %{perl_vendorlib}/Time/
#%{perl_vendorlib}/Time/Local/
%{perl_vendorlib}/Time/Local.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.2000-1
- Updated to version 1.2000.

* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 1.1901-1
- Updated to version 1.1901.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Initial package. (using DAR)
