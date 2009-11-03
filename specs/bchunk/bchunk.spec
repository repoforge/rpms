# $Id$
# Authority: dag
# Upstream: Heikki Hannikainen <hessu$hes,iki,fi>

Summary: Tool to convert from bin/cue CD image format to iso/cdr
Name: bchunk
Version: 1.2.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/File
URL: http://he.fi/bchunk/

Source: http://he.fi/bchunk/bchunk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
binchunker converts a CD image in a ".bin / .cue" format (sometimes
".raw / .cue") to a set of .iso and .cdr tracks. The bin/cue format
is used by some popular non-Unix cd-writing software, but is not
supported on most other CD burning programs.

%prep
%setup

%build
%{__make} CFLAGS="-Wall -Wstrict-prototypes %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bchunk %{buildroot}%{_bindir}/bchunk
%{__install} -Dp -m0644 bchunk.1 %{buildroot}%{_mandir}/man1/bchunk.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/bchunk.1*
%{_bindir}/bchunk

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1.2
- Rebuild for Fedora Core 5.

* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
