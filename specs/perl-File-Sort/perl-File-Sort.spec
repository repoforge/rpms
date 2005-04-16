# $Id$
# Authority: dries
# Upstream: Chris Nandor <cnandor$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Sort

Summary: Sort a file or merge sort multiple files
Name: perl-File-Sort
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Sort/

Source: http://search.cpan.org/CPAN/authors/id/C/CN/CNANDOR/File-Sort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is File::Sort, for sorting files similarly to sort(1).  Written
primarily for MacPerl users who do not have sort(1) and because of memory
limitations cannot sort files in memory, but works on all perls, and can
be useful for portable sorting of large files, or for any system that
doesn't have a sort(1) and is virtual-memory-deprived (including Windows).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/File/Sort.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
