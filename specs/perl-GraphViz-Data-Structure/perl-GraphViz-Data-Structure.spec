# $Id$
# Authority: dries
# Upstream: Joe McMahon <mcmahon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GraphViz-Data-Structure

Summary: Visualise data structures
Name: perl-GraphViz-Data-Structure
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GraphViz-Data-Structure/

Source: http://www.cpan.org/modules/by-module/GraphViz/GraphViz-Data-Structure-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: graphviz
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(GraphViz)
Requires: perl >= 2:5.8.0

%description
GraphViz::Data::Structure produces simple and elegant visualizations
of Perl data structures using Leon Brocard's GraphViz module.

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
%doc BUGS Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/GraphViz::Data::Structure.3pm*
%dir %{perl_vendorlib}/GraphViz/
%dir %{perl_vendorlib}/GraphViz/Data/
#%{perl_vendorlib}/GraphViz/Data/Structure/
%{perl_vendorlib}/GraphViz/Data/Structure.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
