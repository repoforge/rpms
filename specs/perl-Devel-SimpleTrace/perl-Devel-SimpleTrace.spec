# $Id$
# Upstream: Sebastien Aperghis-Tramoni <maddingue@free.fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Devel-SimpleTrace

Summary: See where you code warns and dies using stack traces
Name: perl-Devel-SimpleTrace
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-SimpleTrace/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAPER/Devel-SimpleTrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
Requires: perl(Data::Dumper)

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Devel::SimpleTrace.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Devel/SimpleTrace.pm
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.07-1
- initial package
