# $Id$
# Authority: dries
# Upstream: Joe McMahon <mcmahon$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GraphViz-Data-Structure

Summary: Visualise data structures
Name: perl-GraphViz-Data-Structure
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GraphViz-Data-Structure/

Source: http://search.cpan.org/CPAN/authors/id/M/MC/MCMAHON/GraphViz-Data-Structure-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-GraphViz, graphviz

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/GraphViz/Data/Structure.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
