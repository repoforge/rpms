# $Id$
# Authority: cmr
# Upstream: Gosuke Miyashita, C<< <gosukenator$gmail,com> >>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Trac

Summary: Perl extension for formatting text with Trac Wiki Style
Name: perl-Text-Trac
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Trac/

Source: http://www.cpan.org/modules/by-module/Text/Text-Trac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Base)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(HTML::Entities)
Requires: perl(Class::Accessor::Fast)
Requires: perl(Class::Data::Inheritable)


%description
Perl extension for formatting text with Trac Wiki Style.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::Trac*.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Trac/
%{perl_vendorlib}/Text/Trac.pm

%changelog
* Fri Jun 12 2009 Unknown - 0.15-1
- Initial package. (using DAR)
