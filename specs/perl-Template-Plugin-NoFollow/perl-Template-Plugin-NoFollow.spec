# $Id$
# Authority: dries
# Upstream: Graham TerMarsch <cpan$howlingfrog,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-NoFollow

Summary: Template filter for adding nofollow
Name: perl-Template-Plugin-NoFollow
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-NoFollow/

Source: http://search.cpan.org/CPAN/authors/id/G/GT/GTERMARS/Template-Plugin-NoFollow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Template) >= 2
BuildRequires: perl(Test::More)
Requires: perl(HTML::Parser)
Requires: perl(Template) >= 2

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
TT filter to add rel="nofollow" to all HTML links.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Template::Plugin::NoFollow.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Plugin/
%{perl_vendorlib}/Template/Plugin/NoFollow.pm

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 1.02-1
- Updated to version 1.02.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.000-1
- Initial package.
