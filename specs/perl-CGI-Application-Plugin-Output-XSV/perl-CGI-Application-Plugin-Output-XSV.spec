# $Id$
# Authority: dries
# Upstream: Evan A. Zacks <e-cpan$zacks,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Application-Plugin-Output-XSV

Summary: Generate csv output from a CGI::Application runmode
Name: perl-CGI-Application-Plugin-Output-XSV
Version: 0.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Application-Plugin-Output-XSV/

Source: http://search.cpan.org//CPAN/authors/id/Z/ZA/ZACKSE/CGI-Application-Plugin-Output-XSV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Generate csv output from a CGI::Application runmode.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/CGI::Application::Plugin::Output::XSV*
%{perl_vendorlib}/CGI/Application/Plugin/Output/XSV.pm
%dir %{perl_vendorlib}/CGI/Application/Plugin/Output/
%dir %{perl_vendorlib}/CGI/Application/Plugin/
%dir %{perl_vendorlib}/CGI/Application/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Initial package.
