# $Id$
# Authority: dag
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Handler-Composer

Summary: Another XML printer/writer/generator
Name: perl-XML-Handler-Composer
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Handler-Composer/

Source: http://www.cpan.org/modules/by-module/XML/XML-Handler-Composer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Another XML printer/writer/generator.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/XML::Handler::Composer.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Handler/
#%{perl_vendorlib}/XML/Handler/Composer/
%{perl_vendorlib}/XML/Handler/Composer.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
