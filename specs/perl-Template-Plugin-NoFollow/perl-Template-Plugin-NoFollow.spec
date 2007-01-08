# $Id$
# Authority: dries
# Upstream: Graham TerMarsch <cpan$howlingfrog,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-NoFollow

Summary: Template filter for adding nofollow
Name: perl-Template-Plugin-NoFollow
Version: 1.000
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-NoFollow/

Source: http://search.cpan.org//CPAN/authors/id/G/GT/GTERMARS/Template-Plugin-NoFollow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
TT filter to add rel="nofollow" to all HTML links.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/Template::Plugin::NoFollow*
%{perl_vendorlib}/Template/Plugin/NoFollow.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.000-1
- Initial package.
