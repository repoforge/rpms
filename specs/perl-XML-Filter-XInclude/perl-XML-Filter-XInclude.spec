# $Id$
# Authority: dag
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Filter-XInclude

Summary: Perl module named XML-Filter-XInclude
Name: perl-XML-Filter-XInclude
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Filter-XInclude/

Source: http://www.cpan.org/modules/by-module/XML/XML-Filter-XInclude-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-Filter-XInclude is a Perl module.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP README examples/
%doc %{_mandir}/man3/XML::Filter::XInclude.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Filter/
%{perl_vendorlib}/XML/Filter/XInclude.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
