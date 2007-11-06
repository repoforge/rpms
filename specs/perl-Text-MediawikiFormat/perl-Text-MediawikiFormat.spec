# $Id$
# Authority: dries
# Upstream: Derek Price <derek$ximbiot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-MediawikiFormat

Summary: Translate Wiki markup into other text formats
Name: perl-Text-MediawikiFormat
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-MediawikiFormat/

Source: http://search.cpan.org//CPAN/authors/id/D/DP/DPRICE/Text-MediawikiFormat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Translate Wiki markup into other text formats.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Text::MediawikiFormat*
%{perl_vendorlib}/Text/MediawikiFormat.pm
%{perl_vendorlib}/Text/MediawikiFormat/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
