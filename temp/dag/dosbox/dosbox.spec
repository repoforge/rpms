# Authority: newrpms

Summary: x86 DOS emulator.
Name: dosbox
Version: 0.60
Release: 0
License: GPL
Group: Applications/Emulators
URL: http://dosbox.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: SDL_net-devel

%description
DOSBox is a DOS-emulator that uses the SDL-library which makes DOSBox
very easy to port to different platforms. DOSBox has already been ported
to many different platforms, such as Windows, BeOS, Linux, MacOS X.

DOSBox also emulates CPU:286/386 realmode, Directory FileSystem/XMS/EMS,
a SoundBlaster card for excellent sound compatibility with older games.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Oct 28 2003 Dag Wieers <dag@wieers.com> - 0.60-0
- Fixed the --program-prefix problem. (Edward Rudd)

* Fri Oct 24 2003 Dag Wieers <dag@wieers.com> - 0.60-0
- Initial package. (using DAR)
