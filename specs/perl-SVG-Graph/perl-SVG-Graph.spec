# $Id$
# Authority: dag
# Upstream: Allen Day <allenday$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG-Graph

Summary: Perl module to visualize your data in Scalable Vector Graphics (SVG) format
Name: perl-SVG-Graph
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG-Graph/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-Graph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-SVG-Graph is a Perl module to visualize your data in Scalable Vector
Graphics (SVG) format.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README eg/
%doc %{_mandir}/man3/SVG::Graph.3pm*
%dir %{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG/Frame.pm
%{perl_vendorlib}/SVG/Graph/
%{perl_vendorlib}/SVG/Graph.pm

%changelog
* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 0.02-1
- Updated to version 0.02.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
