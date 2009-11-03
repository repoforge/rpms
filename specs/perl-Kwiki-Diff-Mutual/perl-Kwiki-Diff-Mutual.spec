# $Id$
# Authority: dries
# Upstream: Kazuhiro Osawa <ko$yappo,ne,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-Diff-Mutual

Summary: The selection of revision of both parties of Diff is enabled
Name: perl-Kwiki-Diff-Mutual
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-Diff-Mutual/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-Diff-Mutual-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Install)
BuildRequires: perl(YAML)

%description
The selection of revision of both parties of Diff is enabled.

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
%doc %{_mandir}/man3/Kwiki::Diff::Mutual*
%{perl_vendorlib}/Kwiki/Diff/Mutual.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
