# $Id$
# Authority: dag
# Upstream: Jesse Kornblum <md5deep$jessekornblum,com>

Summary: Compute MD5, SHA-1, SHA-256, Tiger or Whirlpool message digests
Name: md5deep
Version: 1.13
Release: 1%{?dist}
Group: System Environment/Base
License: Public Domain
URL: http://md5deep.sourceforge.net/

Source: http://dl.sf.net/md5deep/md5deep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
md5deep computes the MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digest
for any number of files while optionally recursively digging through the
directory structure. md5deep can also match input files against lists of known
hashes in a variety of formats.

%prep
%setup

%build
%{__make} %{?_smp_mflags} linux OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install \
    BIN="%{buildroot}%{_bindir}" \
    MAN="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man1/md5deep.1*
%doc %{_mandir}/man1/sha1deep.1*
%doc %{_mandir}/man1/sha256deep.1*
%doc %{_mandir}/man1/tigerdeep.1*
%doc %{_mandir}/man1/whirlpooldeep.1*
%{_bindir}/md5deep
%{_bindir}/sha1deep
%{_bindir}/sha256deep
%{_bindir}/tigerdeep
%{_bindir}/whirlpooldeep

%changelog
* Fri Aug 24 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
