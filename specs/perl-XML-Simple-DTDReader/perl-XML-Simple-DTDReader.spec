# $Id$
# Authority: dag
# Upstream: Alex Vandiver <alexmv+pause$mit,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Simple-DTDReader

Summary: Simple XML file reading based on their DTDs
Name: perl-XML-Simple-DTDReader
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Simple-DTDReader/

Source: http://www.cpan.org/modules/by-module/XML/XML-Simple-DTDReader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simple XML file reading based on their DTDs.

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
%doc %{_mandir}/man3/XML::Simple::DTDReader.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Simple/
#%{perl_vendorlib}/XML/Simple/DTDReader/
%{perl_vendorlib}/XML/Simple/DTDReader.pm

%changelog
* Mon Jan 07 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
