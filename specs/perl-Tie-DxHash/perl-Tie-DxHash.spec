# $Id $
# Authority: dries
# Upstream: Kevin Ruscoe <kevin$sapphireoflondon,org>

%define real_name Tie-DxHash
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Keeps insertion order; allows duplicate keys
Name: perl-Tie-DxHash
Version: 1.03
Release: 1.0
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-DxHash/

Source: http://www.cpan.org/modules/by-module/Tie/Tie-DxHash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tie::DxHash implements a hash which preserves insertion order and allows
duplicate keys.  It was written to facilitate the use of more complex
mod_rewrite rules in Apache configuration files written with Perl Sections.
See the module's POD for details.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Tie::DxHash.3pm*
%dir %{perl_vendorlib}/Tie/
%{perl_vendorlib}/Tie/DxHash.pm

%changelog
* Mon Jul 07 2008 Eric Heydrick <erichey@speakeasy.net> - 1.03-1
- Initial package.
