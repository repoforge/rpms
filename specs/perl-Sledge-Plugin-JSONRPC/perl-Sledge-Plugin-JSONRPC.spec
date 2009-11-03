# $Id$
# Authority: dries
# Upstream: Atsushi Kobayashi <nekokak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sledge-Plugin-JSONRPC

Summary: JSONRPC plugin for Sledge
Name: perl-Sledge-Plugin-JSONRPC
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sledge-Plugin-JSONRPC/

Source: http://www.cpan.org/modules/by-module/Sledge/Sledge-Plugin-JSONRPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
JSONRPC plugin for Sledge.

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
%doc Changes README
%doc %{_mandir}/man3/Sledge::Plugin::JSONRPC*
%{perl_vendorlib}/Sledge/Plugin/JSONRPC.pm
%dir %{perl_vendorlib}/Sledge/Plugin/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
