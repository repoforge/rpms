# $Id$
# Authority: dag

Summary: Lossless MP3 volume adjustment tool
Name: mp3gain
%define real_version 1_4_4
Version: 1.4.4
Release: 1.2%{?dist}
License: LGPL
Group: Applications/Multimedia
URL: http://mp3gain.sourceforge.net

Source: http://osdn.dl.sourceforge.net/sourceforge/mp3gain/mp3gain-%{real_version}-src.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same
volume. It does not just do peak normalization, as many normalizers
do. Instead, it does some statistical analysis to determine how loud
the file actually sounds to the human ear. Also, the changes MP3Gain
makes are completely lossless. There is no quality lost in the change
because the program adjusts the mp3 file directly, without decoding
and re-encoding.

%prep
%setup -c %{name}-%{version}

%build
%{__make} CFLAGS="%{optflags} -DHAVE_MEMCPY"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mp3gain %{buildroot}%{_bindir}/mp3gain

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc lgpl.txt
%{_bindir}/mp3gain

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.4-1.2
- Rebuild for Fedora Core 5.

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 1.4.4-1
- Initial package. (using DAR)
