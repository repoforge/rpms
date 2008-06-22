# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa@bulknews.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-Encoding

Summary: Detect encoding of the current terminal
Name: perl-Term-Encoding
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-Encoding/

Source: http://www.cpan.org/modules/by-module/Term/Term-Encoding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Detect encoding of the current terminal.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Term::Encoding.3pm*
%dir %{perl_vendorlib}/Term/
#%{perl_vendorlib}/Term/Encoding/
%{perl_vendorlib}/Term/Encoding.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
