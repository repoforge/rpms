# Authority: dag

%define rversion 550

Summary: Console hex viewer/editor with disassembler.
Name: biew
Version: 5.5.0
Release: 0
Group: Development/Debuggers
License: GPL
URL: http://biew.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/biew/%{name}-%{rversion}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
BIEW (Binary vIEW) is a free, portable, advanced file viewer with
built-in editor for binary, hexadecimal and disassembler modes.

It contains a highlight PentiumIII/K7 Athlon/Cyrix-M2 disassembler,
full preview of MZ, NE, PE, LE, LX, DOS.SYS, NLM, ELF, a.out, arch,
coff32, PharLap, rdoff executable formats, a code guider, and lot of
other features, making it invaluable for examining binary code.

%prep
%setup -n %{name}-%{rversion}

### Change default prefix to %{_prefix}
%{__perl} -pi.orig -e 's|/usr/local|%{_prefix}|' biewlib/sysdep/generic/unix/os_dep.c

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/biew/xlt/ \
			%{buildroot}%{_datadir}/biew/skn/
%{__install} -m0755 biew  %{buildroot}%{_bindir}
%{__install} -m0644 bin_rc/biew.hlp %{buildroot}%{_datadir}/biew/
%{__install} -m0644 bin_rc/skn/*.skn %{buildroot}%{_datadir}/biew/skn/
%{__cp} -auvx bin_rc/xlt/* %{buildroot}%{_datadir}/biew/xlt/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.txt doc/*.en
%{_bindir}/*
%{_datadir}/biew/

%changelog
* Tue Jan 06 2004 Dag Wieers <dag@wieers.com> - 5.5.0-0
- Updated to release 5.5.0.

* Fri Apr 18 2003 Dag Wieers <dag@wieers.com> - 5.3.2-0
- Initial package. (using DAR)
