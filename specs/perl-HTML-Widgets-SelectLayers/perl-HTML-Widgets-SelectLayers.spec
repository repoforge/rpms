# $Id$
# Authority: dries
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Widgets-SelectLayers

Summary: Perl extension for selectable HTML layers
Name: perl-HTML-Widgets-SelectLayers
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Widgets-SelectLayers/

Source: http://search.cpan.org//CPAN/authors/id/I/IV/IVAN/HTML-Widgets-SelectLayers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension for selectable HTML layers.

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
%doc Changes README
%doc %{_mandir}/man3/HTML::Widgets::SelectLayers*
%{perl_vendorlib}/HTML/Widgets/SelectLayers.pm
%{perl_vendorlib}/HTML/Widgets/homepage.pl

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
