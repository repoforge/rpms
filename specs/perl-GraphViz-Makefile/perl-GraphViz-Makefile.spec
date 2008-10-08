# $Id$
# Authority: dries
# Upstream: Slaven Rezi&#263; <slaven$rezic,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GraphViz-Makefile

Summary: Visualize Makefile dependencies
Name: perl-GraphViz-Makefile
Version: 1.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GraphViz-Makefile/

Source: http://www.cpan.org/modules/by-module/GraphViz/GraphViz-Makefile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
dependencies. A sample program for generating Tk output
(tkgvizmakefile) is included.

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
%doc %{_mandir}/man1/tkgvizmakefile.1*
%doc %{_mandir}/man3/GraphViz::Makefile.3pm*
%{_bindir}/tkgvizmakefile
%dir %{perl_vendorlib}/GraphViz/
#%{perl_vendorlib}/GraphViz/Makefile/
%{perl_vendorlib}/GraphViz/Makefile.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
