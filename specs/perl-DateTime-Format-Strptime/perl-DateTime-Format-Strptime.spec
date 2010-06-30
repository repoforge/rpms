# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Strptime

Summary: Parse and format strp and strf time patterns
Name: perl-DateTime-Format-Strptime
Version: 1.2000
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Strptime/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DateTime) >= 0.4304            
BuildRequires: perl(DateTime::Locale) >= 0.45      
BuildRequires: perl(DateTime::TimeZone) >= 0.79    
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Params::Validate) >= 0.64      

%description
This module replicates most of Strptime for DateTime. Strptime is the
unix command that is the reverse of Strftime. While Strftime takes a
DateTime and outputs it in a given format, Strptime takes a DateTime and
a format and returns the DateTime object associated.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
#%{perl_vendorlib}/DateTime/Format/Strptime/
%{perl_vendorlib}/DateTime/Format/Strptime.pm

%changelog
* Wed Jun 30 2010 Steve Huff <shuff@vecna.org> - 1.4000-1
- Updated to version 1.2000.
- Later versions will not build on el5.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 1.1000-1
- Updated to version 1.1000.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 1.0901-1
- Updated to version 1.0901.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.0800-1
- Updated to release 1.0800.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.0702-1
- Updated to release 1.0702.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.0700-1
- Initial package.
