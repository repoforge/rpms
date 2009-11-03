# $Id$
# Authority: dag
# Upstream: Juerd Waalboer <spamcollector_cpan$juerd,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exporter-Tidy

Summary: Another way of exporting symbols
Name: perl-Exporter-Tidy
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exporter-Tidy/

Source: http://www.cpan.org/modules/by-module/Exporter/Exporter-Tidy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Another way of exporting symbols.

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
%doc %{_mandir}/man3/Exporter::Tidy.3pm*
%dir %{perl_vendorlib}/Exporter/
#%{perl_vendorlib}/Exporter/Tidy/
%{perl_vendorlib}/Exporter/Tidy.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
