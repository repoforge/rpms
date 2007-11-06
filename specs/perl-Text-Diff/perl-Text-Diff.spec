# $Id$
# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define real_name Text-Diff
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Perform diffs on files and record sets
Name: perl-Text-Diff
Version: 0.35
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Diff/

Source: http://www.cpan.org/modules/by-module/Text/Text-Diff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Perform diffs on files and record sets.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Diff.pm
%{perl_vendorlib}/Text/Diff

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.35-1.2
- Rebuild for Fedora Core 5.

* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Initial package.

