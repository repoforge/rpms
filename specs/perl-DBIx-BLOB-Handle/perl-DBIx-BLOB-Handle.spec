# $Id$
# Authority: dries
# Upstream: Mark Southern <msouthern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-BLOB-Handle

Summary: Read Database Large Object Binaries from file handles
Name: perl-DBIx-BLOB-Handle
Version: 0.2
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-BLOB-Handle/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-BLOB-Handle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
DBI has a blob_copy_to_file method which takes a file han-
dle argument and copies a database large object binary
(LOB) to this file handle. However, the method is undocu-
mented and faulty. Constructing a similar method yourself
is pretty simple but what if you wished to read the data
and perform operations on it? You could use the DBI's
blob_read method yourself to process chunks of data from
the LOB or even dump its contents into a scalar, but maybe
it would be nice to read the data line by line or piece by
piece from a familiar old filehandle?!

DBIx::BLOB::Handle constructs a tied filehandle that also
extends from IO::Handle and IO::Selectable. It wraps DBI's
blob_read method. By making LOB's available as a file han-
dle to read from we can process the data in a familiar
(perly) way.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/BLOB/Handle.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
