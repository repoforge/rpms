# $Id$

# Authority: dries
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define real_name SVN-Mirror
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Subversion repository mirroring tool
Name: perl-SVN-Mirror
Version: 0.49
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Mirror/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVN-Mirror-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, subversion-perl, perl-Data-UUID, perl-Term-ReadKey
BuildRequires: perl-SVN-Simple

%description
SVN::Mirror is a subversion repository mirroring tool.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES TODO SIGNATURE
%doc %{_mandir}/man?/*
%{_bindir}/svm
%{perl_vendorlib}/SVN/Mirror.pm
%{perl_vendorlib}/SVN/Mirror/*

%changelog
* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Update to release 0.49.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Initial package.
