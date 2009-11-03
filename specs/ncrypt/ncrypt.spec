# $Id$
# Authority: dag

Summary: File encryptor/decryptor/wiper
Name: ncrypt
Version: 0.6.11
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://ncrypt.sourceforge.net/

Source: http://dl.sf.net/sourceforge/ncrypt/ncrypt-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make

%description
Ncrypt is a symmetrical file encryptor/decryptor that gives you the choice of
the top three candidates for AES as the encryption algorithm (Rijndael,
Serpent, Twofish).  Ncrypt also offers two file wiping options, for secure and
unrecoverable deletion of data, including file slack.

Ncrypt is intended to give you security in an insecure environment. If you are
wanting to encrypt files, wishing to hide your activites from prying eyes, and
want to "cover your tracks", Ncrypt is for you.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man8/ncrypt.8*
%{_bindir}/ncrypt

%changelog
* Sun Dec 17 2006 Dag Wieers <dag@wieers.com> - 0.6.11-1
- Initial package. (using DAR)
