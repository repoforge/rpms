# $Id$
# Upstream: Russ Allbery <rra@stanford.edu>
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name ANSIColor

Summary: Color output using ANSI escape sequences
Name: perl-Term-ANSIColor
Version: 3.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-ANSIColor/

Source: http://search.cpan.org/CPAN/authors/id/R/RR/RRA/ANSIColor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc  MANIFEST META.yml README
%doc %{_mandir}/man3/Term::ANSIColor.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Term/ANSIColor.pm
%exclude %{perl_vendorarch}/auto/Term/ANSIColor/.packlist

%changelog
* Tue Feb 08 2011 Christoph Maser <cmaser.gmx.de> - 3.00-1
- initial package
