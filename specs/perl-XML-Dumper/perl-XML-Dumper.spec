# $Id$
# Authority: dag
# Upstream: Mike Wong <mike_w3$pacbell,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Dumper

Summary: Perl module for dumping Perl objects from/to XML
Name: perl-XML-Dumper
Version: 0.81
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Dumper/

Source: http://www.cpan.org/modules/by-module/XML/XML-Dumper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-Dumper is a Perl module for dumping Perl objects from/to XML.

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
%doc %{_mandir}/man3/XML::Dumper.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Dumper.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.81-1
- Initial package. (using DAR)
