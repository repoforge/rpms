# $Id$
# Authority: dries
# Upstream: Junya Kondo <jkondo$hatena,ne,jp>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Hatena

Summary: Perl extension for formatting text with Hatena Style
Name: perl-Text-Hatena
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Hatena/

Source: http://search.cpan.org//CPAN/authors/id/J/JK/JKONDO/Text-Hatena-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Perl extension for formatting text with Hatena Style.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Text::Hatena*
%{perl_vendorlib}/Text/Hatena.pm
%{perl_vendorlib}/Text/Hatena/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
